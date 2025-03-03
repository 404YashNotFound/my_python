# Initialize an empty set to store followers
followers = set()

while True:
    # Take input from the user and convert it to lowercase
    user_input = str.lower(input("Enter your user name to follow (type exit to stop the loop): "))
    
    # Exit condition
    if user_input == 'exit':
        break
    
    # Check if the user is already a follower
    if user_input in followers:
        print("Already a follower")
    else:
        # Add the user to the followers set
        followers.add(user_input)
        print(f"Congrats! {user_input} added as a follower")

# Display final results
print(f"\nThe final Followers: {followers}")
print("The total followers you have: ", len(followers))
