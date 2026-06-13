use dotenv;
use tokio;
use dyncord::{Bot, Intents};
use dyncord::commands::Command;
use dyncord::commands::prefixed::context::PrefixedContext;

#[tokio::main]
async fn main() {
   dotenv::dotenv().ok();
   let token = "DISCORD_TOKEN";

    struct Cmds {
        test: String
    }


    let cmd = Cmds{
        test: "test".to_string()
    };


    let bot = Bot::new(())
    .intents(Intents::GUILD_MESSAGES)
    .intents(Intents::MESSAGE_CONTENT)
    .with_prefix("!")
    .command(Command::prefixed(cmd.test, handle_test));


    bot.run(dotenv::var(token).unwrap()).await.unwrap();

    

}

async fn handle_test(ctx: PrefixedContext) {
    ctx.send("i think it worked");


}


