namespace BillingProvider;

public static class BillingService
{
    public static double CalculateMonthlyBill(double unitPrice, int units)
    {
        if (unitPrice < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(unitPrice));
        }

        if (units < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(units));
        }

        return unitPrice * units;
    }
}
