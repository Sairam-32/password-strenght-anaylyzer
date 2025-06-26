import argparse
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, export_wordlist

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", help="Password to analyze")
    parser.add_argument("-k", "--keywords", nargs="+", help="Keywords for wordlist generation")
    parser.add_argument("-e", "--export", action="store_true", help="Export wordlist to txt")
    args = parser.parse_args()

    if args.password:
        result = analyze_password(args.password)
        print("Score:", result['score'])
        print("Estimated crack time:", result['crack_time'])
        print("Feedback:", result['feedback'])

    if args.keywords:
        wordlist = generate_wordlist(args.keywords)
        print(f"Generated {len(wordlist)} words.")
        if args.export:
            export_wordlist(wordlist)
            print("Wordlist exported.")

if __name__ == "__main__":
    main()