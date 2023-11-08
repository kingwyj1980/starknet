from starknet_py.contract import Contract
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models.chains import StarknetChainId
import time
from decimal import *

client = GatewayClient(net="mainnet")
def get_my_account(private_key,public_key,wallet_address):
    keypair = KeyPair(private_key,
                      public_key)
    return Account(
        address=wallet_address,
        client=client,
        key_pair=keypair,
        chain=StarknetChainId.MAINNET,
    )
eth_contract_address = 0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7
usdc_contract_address = 0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8
jedis_usdc_eth_lp_address=0x04d0390b777b424e43839cd1e744799f3de6c176c7e32c1812a41dbd9c19db6a

def get_eth_contract(my_account):
    eth_contract = Contract(
        address=eth_contract_address,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"from_","type":"felt"},{"name":"to","type":"felt"},{"name":"value","type":"Uint256"}],"keys":[],"name":"Transfer","type":"event"},{"data":[{"name":"owner","type":"felt"},{"name":"spender","type":"felt"},{"name":"value","type":"Uint256"}],"keys":[],"name":"Approval","type":"event"},{"name":"name","type":"function","inputs":[],"outputs":[{"name":"name","type":"felt"}],"stateMutability":"view"},{"name":"symbol","type":"function","inputs":[],"outputs":[{"name":"symbol","type":"felt"}],"stateMutability":"view"},{"name":"totalSupply","type":"function","inputs":[],"outputs":[{"name":"totalSupply","type":"Uint256"}],"stateMutability":"view"},{"name":"decimals","type":"function","inputs":[],"outputs":[{"name":"decimals","type":"felt"}],"stateMutability":"view"},{"name":"balanceOf","type":"function","inputs":[{"name":"account","type":"felt"}],"outputs":[{"name":"balance","type":"Uint256"}],"stateMutability":"view"},{"name":"allowance","type":"function","inputs":[{"name":"owner","type":"felt"},{"name":"spender","type":"felt"}],"outputs":[{"name":"remaining","type":"Uint256"}],"stateMutability":"view"},{"name":"permittedMinter","type":"function","inputs":[],"outputs":[{"name":"minter","type":"felt"}],"stateMutability":"view"},{"name":"initialized","type":"function","inputs":[],"outputs":[{"name":"res","type":"felt"}],"stateMutability":"view"},{"name":"get_version","type":"function","inputs":[],"outputs":[{"name":"version","type":"felt"}],"stateMutability":"view"},{"name":"get_identity","type":"function","inputs":[],"outputs":[{"name":"identity","type":"felt"}],"stateMutability":"view"},{"name":"initialize","type":"function","inputs":[{"name":"init_vector_len","type":"felt"},{"name":"init_vector","type":"felt*"}],"outputs":[]},{"name":"transfer","type":"function","inputs":[{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"transferFrom","type":"function","inputs":[{"name":"sender","type":"felt"},{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"approve","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"increaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"added_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"decreaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"subtracted_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"permissionedMint","type":"function","inputs":[{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[]},{"name":"permissionedBurn","type":"function","inputs":[{"name":"account","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[]}],
        provider=my_account,
    )

    return eth_contract

def get_usdc_contract(my_account):

    usdc_contract = Contract(
        address=usdc_contract_address,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"from_","type":"felt"},{"name":"to","type":"felt"},{"name":"value","type":"Uint256"}],"keys":[],"name":"Transfer","type":"event"},{"data":[{"name":"owner","type":"felt"},{"name":"spender","type":"felt"},{"name":"value","type":"Uint256"}],"keys":[],"name":"Approval","type":"event"},{"name":"name","type":"function","inputs":[],"outputs":[{"name":"name","type":"felt"}],"stateMutability":"view"},{"name":"symbol","type":"function","inputs":[],"outputs":[{"name":"symbol","type":"felt"}],"stateMutability":"view"},{"name":"totalSupply","type":"function","inputs":[],"outputs":[{"name":"totalSupply","type":"Uint256"}],"stateMutability":"view"},{"name":"decimals","type":"function","inputs":[],"outputs":[{"name":"decimals","type":"felt"}],"stateMutability":"view"},{"name":"balanceOf","type":"function","inputs":[{"name":"account","type":"felt"}],"outputs":[{"name":"balance","type":"Uint256"}],"stateMutability":"view"},{"name":"allowance","type":"function","inputs":[{"name":"owner","type":"felt"},{"name":"spender","type":"felt"}],"outputs":[{"name":"remaining","type":"Uint256"}],"stateMutability":"view"},{"name":"permittedMinter","type":"function","inputs":[],"outputs":[{"name":"minter","type":"felt"}],"stateMutability":"view"},{"name":"initialized","type":"function","inputs":[],"outputs":[{"name":"res","type":"felt"}],"stateMutability":"view"},{"name":"get_version","type":"function","inputs":[],"outputs":[{"name":"version","type":"felt"}],"stateMutability":"view"},{"name":"get_identity","type":"function","inputs":[],"outputs":[{"name":"identity","type":"felt"}],"stateMutability":"view"},{"name":"initialize","type":"function","inputs":[{"name":"init_vector_len","type":"felt"},{"name":"init_vector","type":"felt*"}],"outputs":[]},{"name":"transfer","type":"function","inputs":[{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"transferFrom","type":"function","inputs":[{"name":"sender","type":"felt"},{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"approve","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"increaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"added_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"decreaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"subtracted_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"permissionedMint","type":"function","inputs":[{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[]},{"name":"permissionedBurn","type":"function","inputs":[{"name":"account","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[]}],
        provider=my_account,
    )

    return usdc_contract


def get_jedis_usdc_eth_lp_contract(my_account):

    jedis_usdc_eth_lp = Contract(
        address=jedis_usdc_eth_lp_address,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"name":"initializer","type":"function","inputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"name","type":"function","inputs":[],"outputs":[{"name":"name","type":"felt"}],"stateMutability":"view"},{"name":"symbol","type":"function","inputs":[],"outputs":[{"name":"symbol","type":"felt"}],"stateMutability":"view"},{"name":"totalSupply","type":"function","inputs":[],"outputs":[{"name":"totalSupply","type":"Uint256"}],"stateMutability":"view"},{"name":"decimals","type":"function","inputs":[],"outputs":[{"name":"decimals","type":"felt"}],"stateMutability":"view"},{"name":"balanceOf","type":"function","inputs":[{"name":"account","type":"felt"}],"outputs":[{"name":"balance","type":"Uint256"}],"stateMutability":"view"},{"name":"allowance","type":"function","inputs":[{"name":"owner","type":"felt"},{"name":"spender","type":"felt"}],"outputs":[{"name":"remaining","type":"Uint256"}],"stateMutability":"view"},{"name":"token0","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"token1","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"get_reserves","type":"function","inputs":[],"outputs":[{"name":"reserve0","type":"Uint256"},{"name":"reserve1","type":"Uint256"},{"name":"block_timestamp_last","type":"felt"}],"stateMutability":"view"},{"name":"price_0_cumulative_last","type":"function","inputs":[],"outputs":[{"name":"res","type":"Uint256"}],"stateMutability":"view"},{"name":"price_1_cumulative_last","type":"function","inputs":[],"outputs":[{"name":"res","type":"Uint256"}],"stateMutability":"view"},{"name":"klast","type":"function","inputs":[],"outputs":[{"name":"res","type":"Uint256"}],"stateMutability":"view"},{"name":"transfer","type":"function","inputs":[{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"transferFrom","type":"function","inputs":[{"name":"sender","type":"felt"},{"name":"recipient","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"approve","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"amount","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"increaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"added_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"decreaseAllowance","type":"function","inputs":[{"name":"spender","type":"felt"},{"name":"subtracted_value","type":"Uint256"}],"outputs":[{"name":"success","type":"felt"}]},{"name":"mint","type":"function","inputs":[{"name":"to","type":"felt"}],"outputs":[{"name":"liquidity","type":"Uint256"}]},{"name":"burn","type":"function","inputs":[{"name":"to","type":"felt"}],"outputs":[{"name":"amount0","type":"Uint256"},{"name":"amount1","type":"Uint256"}]},{"name":"swap","type":"function","inputs":[{"name":"amount0Out","type":"Uint256"},{"name":"amount1Out","type":"Uint256"},{"name":"to","type":"felt"},{"name":"data_len","type":"felt"},{"name":"data","type":"felt*"}],"outputs":[]},{"name":"skim","type":"function","inputs":[{"name":"to","type":"felt"}],"outputs":[]},{"name":"sync","type":"function","inputs":[],"outputs":[]}],
        provider=my_account,
    )
    return jedis_usdc_eth_lp

def get_eth_balance(my_account):
    eth_contract = get_eth_contract(my_account)
    return eth_contract.functions["balanceOf"].call_sync(my_account.address)[0]


def get_usdc_balance(my_account):
    usdc_contract = get_usdc_contract(my_account)
    return usdc_contract.functions["balanceOf"].call_sync(my_account.address)[0]



def get_jedis_contract(my_account):
    return Contract(
        address=0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"implementation","type":"felt"}],"keys":[],"name":"Upgraded","type":"event"},{"data":[{"name":"previousAdmin","type":"felt"},{"name":"newAdmin","type":"felt"}],"keys":[],"name":"AdminChanged","type":"event"},{"name":"initializer","type":"function","inputs":[{"name":"factory","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"factory","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"sort_tokens","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"}],"outputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"}],"stateMutability":"view"},{"name":"quote","type":"function","inputs":[{"name":"amountA","type":"Uint256"},{"name":"reserveA","type":"Uint256"},{"name":"reserveB","type":"Uint256"}],"outputs":[{"name":"amountB","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountOut","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountIn","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amounts_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"get_amounts_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"add_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"amountADesired","type":"Uint256"},{"name":"amountBDesired","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"},{"name":"liquidity","type":"Uint256"}]},{"name":"remove_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"liquidity","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"}]},{"name":"swap_exact_tokens_for_tokens","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"amountOutMin","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]},{"name":"swap_tokens_for_exact_tokens","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"amountInMax","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]}],
        provider=my_account,
    )

def addliquidity_jedis(my_account,usdc_amount_in):
    print("jedis add liquidity：")
    print("address:" + str(hex(my_account.address)))

    usdc_balance = get_usdc_balance(my_account)
    print("usdc balance" + str(usdc_balance))


    usdc_amount_in_min = int(usdc_amount_in/1.024)

    eth_amount_in = get_eth_amounts_out_min(my_account,usdc_amount_in)
    eth_amount_in_min = int(usdc_amount_in_min/1.024)

    eth_contract = get_eth_contract(my_account)
    eth_approve_call = eth_contract.functions["approve"].prepare(0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023, eth_amount_in)
    usdc_contract = get_usdc_contract(my_account)
    usdc_approve_call = usdc_contract.functions["approve"].prepare(0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023, usdc_amount_in)
    deadline = (int(time.time()) + 60 * 60)
    contract = get_jedis_contract(my_account)
    addliquidity_call = contract.functions["add_liquidity"].prepare(usdc_contract_address,eth_contract_address,usdc_amount_in,eth_amount_in,usdc_amount_in_min,eth_amount_in_min,my_account.address,deadline)
    response = my_account.execute_sync([eth_approve_call, usdc_approve_call,addliquidity_call], auto_estimate=True)
    print(str(hex(response.transaction_hash)))
    print("result：" + str(hex(response.transaction_hash)))


def removeliquidity_jedis(my_account):
    print("remove liquidity：")
    print(hex(my_account.address))

    contract = get_jedis_usdc_eth_lp_contract(my_account)

    totalshares = (contract.functions["totalSupply"].call_sync()).totalSupply
    myshares = (contract.functions["balanceOf"].call_sync(my_account.address)).balance
    reserves = (contract.functions["get_reserves"].call_sync())

    token_a_reserves = reserves.reserve0
    token_b_reserves = reserves.reserve1
    #
    remove_shares = myshares
    amount_min_a = int(remove_shares*token_a_reserves/totalshares/1.02)
    amount_min_b = int(remove_shares*token_b_reserves/totalshares/1.02)
    #
    print(remove_shares)
    print(amount_min_a)
    print(amount_min_b)
    deadline = (int(time.time()) + 60 * 60)
    lp_contract = get_jedis_usdc_eth_lp_contract(my_account)
    lp_approve_call = lp_contract.functions["approve"].prepare(
        0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023, remove_shares)
    contract = get_jedis_contract(my_account)
    removeliquidity_call = contract.functions["remove_liquidity"].prepare(eth_contract_address,usdc_contract_address,
                                                remove_shares,amount_min_a, amount_min_b,my_account.address,deadline)
    response = my_account.execute_sync([lp_approve_call, removeliquidity_call], auto_estimate=True)
    print(str(hex(response.transaction_hash)))
    print("交易结果：" + str(hex(response.transaction_hash)))


def swap_jedis_usdc2eth(my_account,amount_in):
    print("jedis usdc2et：")
    print("address:" + str(hex(my_account.address)))
    my_account.set_fee_multiplier(3)
    usdc_balance = get_usdc_balance(my_account)
    usdc_balance = usdc_balance
    print("usdc balance"+str(usdc_balance))
    usdc_contract = get_usdc_contract(my_account)
    approve_call = usdc_contract.functions["approve"].prepare(0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023, amount_in)
    contract = Contract(
        address=0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"implementation","type":"felt"}],"keys":[],"name":"Upgraded","type":"event"},{"data":[{"name":"previousAdmin","type":"felt"},{"name":"newAdmin","type":"felt"}],"keys":[],"name":"AdminChanged","type":"event"},{"name":"initializer","type":"function","inputs":[{"name":"factory","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"factory","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"sort_tokens","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"}],"outputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"}],"stateMutability":"view"},{"name":"quote","type":"function","inputs":[{"name":"amountA","type":"Uint256"},{"name":"reserveA","type":"Uint256"},{"name":"reserveB","type":"Uint256"}],"outputs":[{"name":"amountB","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountOut","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountIn","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amounts_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"get_amounts_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"add_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"amountADesired","type":"Uint256"},{"name":"amountBDesired","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"},{"name":"liquidity","type":"Uint256"}]},{"name":"remove_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"liquidity","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"}]},{"name":"swap_exact_tokens_for_tokens","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"amountOutMin","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]},{"name":"swap_tokens_for_exact_tokens","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"amountInMax","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]}],
        provider=my_account,
    )

    path = [
        0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8,
        0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7
    ]
    amount_out_min = get_eth_amounts_out_min(my_account,amount_in)
    deadline = (int(time.time()) + 60 * 60)
    swap_call = contract.functions["swap_exact_tokens_for_tokens"].prepare(amount_in,amount_out_min,path,my_account.address,deadline)

    response = my_account.execute_sync([approve_call, swap_call], auto_estimate=True)
    print(str(hex(response.transaction_hash)))
    print("result："+str(hex(response.transaction_hash)))

def swap_jedis(my_account,amount_in):
    eth_balance = get_eth_balance(my_account)
    print(eth_balance)
    print("swap_jedis ：" + str(amount_in))
    print("address:" + str(hex(my_account.address)))
    my_account.set_fee_multiplier(3)
    amount_in = int(Decimal(str(amount_in)) * Decimal("1e18"))
    eth_contract = get_eth_contract(my_account)
    approve_call = eth_contract.functions["approve"].prepare(
        0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023, amount_in)
    contract = Contract(
        address=0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"implementation","type":"felt"}],"keys":[],"name":"Upgraded","type":"event"},{"data":[{"name":"previousAdmin","type":"felt"},{"name":"newAdmin","type":"felt"}],"keys":[],"name":"AdminChanged","type":"event"},{"name":"initializer","type":"function","inputs":[{"name":"factory","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"factory","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"sort_tokens","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"}],"outputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"}],"stateMutability":"view"},{"name":"quote","type":"function","inputs":[{"name":"amountA","type":"Uint256"},{"name":"reserveA","type":"Uint256"},{"name":"reserveB","type":"Uint256"}],"outputs":[{"name":"amountB","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountOut","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountIn","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amounts_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"get_amounts_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"add_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"amountADesired","type":"Uint256"},{"name":"amountBDesired","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"},{"name":"liquidity","type":"Uint256"}]},{"name":"remove_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"liquidity","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"}]},{"name":"swap_exact_tokens_for_tokens","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"amountOutMin","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]},{"name":"swap_tokens_for_exact_tokens","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"amountInMax","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]}],
        provider=my_account,
    )
    path = [
        0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7,
        0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8
    ]
    amount_out_min = get_amounts_out_min(my_account,amount_in)
    deadline = (int(time.time()) + 60 * 60)
    swap_call = contract.functions["swap_exact_tokens_for_tokens"].prepare(amount_in,amount_out_min,path,my_account.address,deadline)

    response = my_account.execute_sync([approve_call, swap_call], auto_estimate=True)
    print(str(hex(response.transaction_hash)))
    print("result："+str(hex(response.transaction_hash)))

def get_amounts_out_min(my_account,amount_in):
    path = [
        0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7,
        0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8
    ]
    contract = Contract(
        address=0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"implementation","type":"felt"}],"keys":[],"name":"Upgraded","type":"event"},{"data":[{"name":"previousAdmin","type":"felt"},{"name":"newAdmin","type":"felt"}],"keys":[],"name":"AdminChanged","type":"event"},{"name":"initializer","type":"function","inputs":[{"name":"factory","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"factory","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"sort_tokens","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"}],"outputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"}],"stateMutability":"view"},{"name":"quote","type":"function","inputs":[{"name":"amountA","type":"Uint256"},{"name":"reserveA","type":"Uint256"},{"name":"reserveB","type":"Uint256"}],"outputs":[{"name":"amountB","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountOut","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountIn","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amounts_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"get_amounts_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"add_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"amountADesired","type":"Uint256"},{"name":"amountBDesired","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"},{"name":"liquidity","type":"Uint256"}]},{"name":"remove_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"liquidity","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"}]},{"name":"swap_exact_tokens_for_tokens","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"amountOutMin","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]},{"name":"swap_tokens_for_exact_tokens","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"amountInMax","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]}],
        provider=my_account,
    )
    out = contract.functions["get_amounts_out"].call_sync(amount_in, path)
    amount_out_min = int(out[0][1] * 0.98)
    return amount_out_min

def get_eth_amounts_out_min(my_account,amount_in):
    path = [
        0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8,
        0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7
    ]
    contract = Contract(
        address=0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023,
        abi=[{"name":"Uint256","size":2,"type":"struct","members":[{"name":"low","type":"felt","offset":0},{"name":"high","type":"felt","offset":1}]},{"data":[{"name":"implementation","type":"felt"}],"keys":[],"name":"Upgraded","type":"event"},{"data":[{"name":"previousAdmin","type":"felt"},{"name":"newAdmin","type":"felt"}],"keys":[],"name":"AdminChanged","type":"event"},{"name":"initializer","type":"function","inputs":[{"name":"factory","type":"felt"},{"name":"proxy_admin","type":"felt"}],"outputs":[]},{"name":"factory","type":"function","inputs":[],"outputs":[{"name":"address","type":"felt"}],"stateMutability":"view"},{"name":"sort_tokens","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"}],"outputs":[{"name":"token0","type":"felt"},{"name":"token1","type":"felt"}],"stateMutability":"view"},{"name":"quote","type":"function","inputs":[{"name":"amountA","type":"Uint256"},{"name":"reserveA","type":"Uint256"},{"name":"reserveB","type":"Uint256"}],"outputs":[{"name":"amountB","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountOut","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amount_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"reserveIn","type":"Uint256"},{"name":"reserveOut","type":"Uint256"}],"outputs":[{"name":"amountIn","type":"Uint256"}],"stateMutability":"view"},{"name":"get_amounts_out","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"get_amounts_in","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}],"stateMutability":"view"},{"name":"add_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"amountADesired","type":"Uint256"},{"name":"amountBDesired","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"},{"name":"liquidity","type":"Uint256"}]},{"name":"remove_liquidity","type":"function","inputs":[{"name":"tokenA","type":"felt"},{"name":"tokenB","type":"felt"},{"name":"liquidity","type":"Uint256"},{"name":"amountAMin","type":"Uint256"},{"name":"amountBMin","type":"Uint256"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amountA","type":"Uint256"},{"name":"amountB","type":"Uint256"}]},{"name":"swap_exact_tokens_for_tokens","type":"function","inputs":[{"name":"amountIn","type":"Uint256"},{"name":"amountOutMin","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]},{"name":"swap_tokens_for_exact_tokens","type":"function","inputs":[{"name":"amountOut","type":"Uint256"},{"name":"amountInMax","type":"Uint256"},{"name":"path_len","type":"felt"},{"name":"path","type":"felt*"},{"name":"to","type":"felt"},{"name":"deadline","type":"felt"}],"outputs":[{"name":"amounts_len","type":"felt"},{"name":"amounts","type":"Uint256*"}]}],
        provider=my_account,
    )
    out = contract.functions["get_amounts_out"].call_sync(amount_in, path)
    amount_out_min = int(out[0][1] * 0.98)
    return amount_out_min
