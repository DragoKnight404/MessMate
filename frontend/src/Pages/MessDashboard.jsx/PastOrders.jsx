import OrderHistory from './OrderHistory'

const PastOrders = () => {
  return (
    <div className="layout-content-container flex flex-col max-w-[960px] flex-1">
    <div className="flex flex-wrap justify-between gap-3 p-4">
      <p className="text-blackText tracking-light text-[32px] font-bold leading-tight min-w-72">
        Orders Dashboard
      </p>
    </div>

    {/* <h3 className="text-blackText text-lg font-bold leading-tight tracking-[-0.015em] px-4 pb-2 pt-4">
      Current Orders
    </h3> */}

    {/* <h3 className="text-reddish text-lg font-bold leading-tight tracking-[-0.015em] px-4 pb-2 pt-4">
      Orders
    </h3> */}

    <div className="px-4 py-3">
      <label className="flex flex-col min-w-40 h-12 w-full">
        <div className="flex w-full flex-1 items-stretch rounded-xl h-full">
          <div className="text-colorText flex border-none bg-background items-center justify-center pl-4 rounded-l-xl border-r-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24px"
              height="24px"
              fill="currentColor"
              viewBox="0 0 256 256"
            >
              <path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z" />
            </svg>
          </div>
          <input
            placeholder="Search orders"
            className="flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-blackText focus:outline-0 focus:ring-0 border-none bg-background h-full placeholder:text-colorText px-4 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal"
          />
        </div>
      </label>
    </div>
    <div className="px-4 py-3">
      <OrderHistory />
    </div>


  </div>
  )
}

export default PastOrders