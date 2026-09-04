export class CreateBillingReportDto {
    customerId: string;
    /**
     * If the Free Trial is ending
     * <br><br>
     * Example: `true`
     * @example true
     */
    freeTrialEnd?: boolean;

    offeringId?: string;
    businessID: string;
    /**
     * The billing date override for a benchmark billing end date to run
     * <br><br>
     *
     * Example: `2021-03-01`
     * @example 2021-03-01
     *
     */
    endDateOverride?: string;
    /**
     *
     * The billing date override for a benchmark billing start date to run
     * <br><br>
     *
     * Example: `2021-02-01`
     * @example 2021-02-01
     **/
    startDateOverride?: string;
}
