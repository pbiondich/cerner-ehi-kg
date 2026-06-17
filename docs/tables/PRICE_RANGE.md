# PRICE_RANGE

> Pricing schedules for PharmNet

**Description:** Price Range  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_FEE` | DOUBLE |  |  | Fee charged for administration of medication |
| 2 | `COPAY` | DOUBLE |  |  | Amount of isurance copay |
| 3 | `COPAY_PERCENT` | DOUBLE |  |  | Insurance copay percentage |
| 4 | `FROM_COST` | DOUBLE | NOT NULL |  | Bottom tier of price range |
| 5 | `MARKDOWN` | DOUBLE |  |  | Amount of Markdown |
| 6 | `MARK_UP` | DOUBLE |  |  | Mark up on each product dispensed |
| 7 | `MIN_PRICE` | DOUBLE |  |  | Minimum price charged regardless of calculated price |
| 8 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Oracle assigned key for table |
| 9 | `ROUND_UP` | DOUBLE |  |  | Rounding factor for calculated price |
| 10 | `SERVICE_FEE` | DOUBLE |  |  | Dispensing fee for each dispense |
| 11 | `SERVICE_FEE_PERCENT` | DOUBLE |  |  | Service fee percentage |
| 12 | `TO_COST` | DOUBLE |  |  | Upper limit for price range |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

