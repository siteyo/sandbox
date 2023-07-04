use clap::{Args, Parser, Subcommand};

#[derive(Parser)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Add(AddArgs),
    Delete {
        #[arg(short, long)]
        name: Option<String>,
    },
}

#[derive(Args)]
struct AddArgs {
    #[arg(short, long)]
    name: String,
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Add(args) => {
            println!("myapp add: {:?}", args.name)
        }
        Commands::Delete { name } => {
            println!("myapp delete: {:?}", name)
        }
    }
}
