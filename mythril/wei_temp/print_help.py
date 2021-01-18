from mythril.laser.smt import symbol_factory


def print_final_global_state( global_states: list):
    print("============== final global state =============================")
    print(f'\t the number of final global states:{len(global_states)}')
    # for state in global_states:
    #     print("============== final global state =============================")
    #
    #     print("\t---------------- pc  --------------------------")
    #     print(f'\t {state.mstate.pc}')
    #
    #     print("\t---------------- chainid  --------------------------")
    #     print(f'\t {state.environment.chainid}')
    #
    #     print("\t---------------- active_function_name  --------------------------")
    #     print(f'\t {state.environment.active_function_name}')
    #
    #     print("\t---------------- accounts  --------------------------")
    #     for k in state.world_state.accounts.keys():
    #         print(f'\t{k}')
    #         print(f'\t\tnonce: {state.world_state.accounts.get(k).nonce}')
    #
    #         print("\t\t---------------- balance  --------------------------")
    #         # for b in open_state.accounts.get(k).balance.__str__():
    #         print(f'\t\t{state.world_state.accounts.get(k).balance().value}')
    #
    #         print("\t\t---------------- storage --------------------------")
    #         for s in range(8):
    #             print(f'\t\t{state.world_state.accounts.get(k).storage.__getitem__(symbol_factory.BitVecVal(s, 256))}')
    #
    #     print("\t---------------- constraints  --------------------------")
    #     for c1 in state.world_state.constraints.as_list:
    #         print(f'\t {c1}')
    #
    #     print("\t---------------- transaction_sequence --------------------------")
    #     for c2 in state.world_state.transaction_sequence:
    #         print(f'\t {c2}')


def print_open_states(open_states:list):
    for open_state in open_states:
        print("============== open states =============================")
        #
        # for k,v in open_state.accounts.items():
        #     print(f'{k}  {v}')
        print("\t---------------- accounts  --------------------------")
        for k in open_state.accounts.keys():
            print(f'\t{k}')
            print(f'\t\tnonce: {open_state.accounts.get(k).nonce}')

            print("\t\t---------------- balance  --------------------------")
            # for b in open_state.accounts.get(k).balance.__str__():
            print(f'\t\t{open_state.accounts.get(k).balance().value}')

            print("\t\t---------------- storage --------------------------")
            for s in range(8):
                print(f'\t\t{open_state.accounts.get(k).storage.__getitem__(symbol_factory.BitVecVal(s, 256))}')

        # for v in open_state.accounts.values():
        #     print(f'\t{v}')

        print("\t---------------- constraints  --------------------------")
        for c1 in open_state.constraints.as_list:
            print(f'\t{c1}')
        print("\t---------------- transaction_sequence --------------------------")
        for c2 in open_state.transaction_sequence:
            print(f'\t {c2}')
