##################################################################
# Feel free to add helpfull functions to be used with your puzzles
##################################################################



#Retrieve the hash_answers
exec(open('files/hash_answers.py').read())
def submit_answer(answer, prob_num=None):
    '''
    This function is used to compare your answer to the correct one
    '''
    import hashlib
    import base64
    from IPython.core.display import display, HTML

    if isinstance(answer, float):
        if round(answer) == answer:
            answer = str(int(answer))
    answer = str(answer)

    scramble = 'XQukJWJ1If7HuHArsITkAEHAfaHbtTfEmnjzPA9CEoy5QDzVnC'
    def gen_hash():
        hashable = scramble + str(prob_num) + answer
        m = hashlib.sha256()
        m.update(hashable.encode('utf-8'))
        return base64.b64encode(m.digest()).decode('utf-8')

    if gen_hash() == hash_answers[prob_num]:
        display(HTML('<font color=#0acc2d size="7">&#x2713;</font>'+answer))
    else:
        display(HTML('<font color=#cc0a0a size="7">&#x2717;</font>'+answer))