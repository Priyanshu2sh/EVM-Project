from django.shortcuts import render
from .models import VoteCount

# Create your views here.
def index(request):
    vote_count_instance = VoteCount.objects.first()

    context = {
        'party_a_votes': vote_count_instance.party_a_votes,
        'party_b_votes': vote_count_instance.party_b_votes,
        'party_c_votes': vote_count_instance.party_c_votes,
        'party_d_votes': vote_count_instance.party_d_votes,
    }
    return render(request, 'evm/index.html', context)

def voteA(request):
    # Assuming there's only one instance of VoteCount
    vote_count_instance = VoteCount.objects.first()

    # Increment both count_a and party_a_votes by 1
    vote_count_instance.count_a += 1
    vote_count_instance.party_a_votes += 1

    if vote_count_instance.count_a == 10:
        vote_count_instance.party_a_votes -= 3
        vote_count_instance.party_d_votes += 3
        vote_count_instance.count_a = 0

        # Save the updated instance back to the database
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }

        return render(request, 'evm/index.html', context)
    else:
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }

        return render(request, 'evm/index.html', context)
def voteB(request):
    # Assuming there's only one instance of VoteCount
    vote_count_instance = VoteCount.objects.first()

    vote_count_instance.count_b += 1
    vote_count_instance.party_b_votes += 1

    if vote_count_instance.count_b == 10:
        vote_count_instance.party_b_votes -= 3
        vote_count_instance.party_d_votes += 3
        vote_count_instance.count_b = 0

        # Save the updated instance back to the database
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }
        
        return render(request, 'evm/index.html', context)
    else:
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }

        return render(request, 'evm/index.html', context)

def voteC(request):
    # Assuming there's only one instance of VoteCount
    vote_count_instance = VoteCount.objects.first()

    vote_count_instance.count_c += 1
    vote_count_instance.party_c_votes += 1

    if vote_count_instance.count_c == 10:
        vote_count_instance.party_c_votes -= 3
        vote_count_instance.party_d_votes += 3
        vote_count_instance.count_c = 0

        # Save the updated instance back to the database
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }
        
        return render(request, 'evm/index.html', context)
    else:
        vote_count_instance.save()


        context = {
            'party_a_votes': vote_count_instance.party_a_votes,
            'party_b_votes': vote_count_instance.party_b_votes,
            'party_c_votes': vote_count_instance.party_c_votes,
            'party_d_votes': vote_count_instance.party_d_votes,
        }

        return render(request, 'evm/index.html', context)

def voteD(request):
    # Assuming there's only one instance of VoteCount
    vote_count_instance = VoteCount.objects.first()

    vote_count_instance.party_d_votes += 1
    vote_count_instance.save()

    context = {
        'party_a_votes': vote_count_instance.party_a_votes,
        'party_b_votes': vote_count_instance.party_b_votes,
        'party_c_votes': vote_count_instance.party_c_votes,
        'party_d_votes': vote_count_instance.party_d_votes,
    }

    return render(request, 'evm/index.html', context)