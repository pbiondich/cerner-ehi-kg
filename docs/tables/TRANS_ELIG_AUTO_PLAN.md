# TRANS_ELIG_AUTO_PLAN

> Table is used to store the rule information necessary for automatic encounter or person health plan relatonship additions or updates that could not be processed immediately upon the receival of eligibility response.

**Description:** Transaction Eligibility Automatic Health Plan Deferred Rule Processing  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_SECONDARY_INQ_IND` | DOUBLE |  |  | Indicates if a secondary eligibility inquiry should be published automatically. |
| 2 | `AUTO_SECONDARY_INQ_RANGE_DAYS` | DOUBLE |  |  | The time range, in calendar days, used to search for past eligibility inquiries when determining if an automatic secondary eligibility inquiry should be published. If the Auto Secondary Inquiry Indicator is 1 and the Auto Secondary Inquiry Range Days is 0, ignore past eligibility inquiries and automatically publish a secondary inquiry. |
| 3 | `AUTO_SEC_INQ_BEG_COV_DT_ISO` | VARCHAR(10) |  |  | The plan coverage date for which eligibility is requested of the payer when publishing an automatic secondary eligibility inquiry. Date format is YYYY-MM-DD. Currently only a range of a single day is supported. |
| 4 | `GROUP_NAME` | VARCHAR(200) |  |  | The group name associated to the health plan identifier returned by the eligibility response rule. Used for automated processing of the health plan relationship. |
| 5 | `GROUP_NBR` | VARCHAR(100) |  |  | The group number associated to the health plan identifier returned by the eligibility response rule. Used for automated processing of the health plan relationship. |
| 6 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The Millennium health plan identifier returned by the eligibility response rules to be used for automated processing of the health plan relationship. |
| 7 | `MEMBER_NBR` | VARCHAR(100) |  |  | The member number associated to the health plan identifier returned by the eligibility response rule. Used for automated processing of the health plan relationship. |
| 8 | `RULE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of rule used to determine how the health plan relationship should be processed based of the eligibility response. For example add or update. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | Defines the current state of the eligibility response rule to determine if processing is still necessary. |
| 10 | `TRANSACTION_ELIGIBILITY_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the transaction_eligibility table to which this auto plan is related. |
| 11 | `TRANS_ELIG_AUTO_PLAN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the TRANS_ELIG_AUTO_PLAN table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `TRANSACTION_ELIGIBILITY_ID` | [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `TRANSACTION_ELIGIBILITY_ID` |

