use std::env;
use dotenv;
use tokio;
use dyncord::{Bot, Intents};
use dyncord::commands::Command; 
use dyncord::commands::prefixed::context::PrefixedContext;
use sysinfo;
use sysinfo::{System};


#[tokio::main]
async fn main() {
   dotenv::dotenv().ok();
   let token = "DISCORD_TOKEN";


   /*
   these must all return strings atm.
   i dont know much about rust rn, so thats why
   
    */
    struct Cmds {
        test: String,
        implm: String

    }


    let cmd = Cmds{
        test: "test".to_string(),
        implm: "implinfo".to_string()
    }; 

    let bot = Bot::new(())
    .intents(Intents::GUILD_MESSAGES)
    .intents(Intents::MESSAGE_CONTENT)
    .with_prefix("!")
    // .command(Command::prefixed("test", handle_test));\
    .command(Command::prefixed(cmd.implm, implmentation_info))
    .command(Command::prefixed(cmd.test, handle_test));


    bot.run(env::var(token).expect("nigger moment v2")).await.unwrap();
    
    

}

async fn handle_test(ctx: PrefixedContext) {
    ctx.send("i think it worked").await
    .expect("no msg");


}


async fn implmentation_info(ctx: PrefixedContext) {
    const VERSION_INFO: &str = "1.0.0";
    let mut sys = System::new_all();
    let os = System::os_version().unwrap_or_default();

    sys.refresh_all();


    ctx.send(format!("
    # Zavati Script Loader Info 

```
OS: {}
Version: {}
RAM: {:?}
Cores: {}
CPU: {:?}
```
    ", os, VERSION_INFO, sys.total_memory(), num_cpus::get_physical(), sys.cpus().first().map(|cpu| cpu.brand()))).await
    .expect("no msg");
}