# PRICE_SCHED

> Describes Price Schedules.

**Description:** Price Schedule  
**Table type:** REFERENCE  
**Primary key:** `PRICE_SCHED_ID`  
**Columns:** 35  
**Referenced by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_MARKUP_TO_FLAG` | DOUBLE | NOT NULL |  | Indicates whether markup and fees are calculated on the entire dose or by product units (applies only to records with Pharm_ind = 1) 0 - Dose, 1 - Product Unit |
| 6 | `APPLY_SVC_FEE_IND` | DOUBLE |  |  | Indicates whether or not to apply a Service Fee (valid only on records w/pharm_ind = 1). |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `COMPLIANCE_CHECK_IND` | DOUBLE |  |  | Used for compliance checking for rate |
| 9 | `CONVERSION_FACTOR_CD` | DOUBLE | NOT NULL |  | This column in longer used |
| 10 | `COST_BASIS_CD` | DOUBLE | NOT NULL |  | The code value from 4050 indicating the cost basis to be used in calculating PharmNet charges. |
| 11 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the price schedule was created. |
| 12 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person ID from the prsnl table who created the price schedule. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FORMULA_TYPE_FLG` | DOUBLE |  |  | Indicates whether the formula type is order or ingredient (applies only to records with pharm_ind = 1) |
| 15 | `MARKUP_LEVEL_FLG` | DOUBLE |  |  | Indicates where the markup level is order or ingredient (applies only to records w/pharm_ind = 1). |
| 16 | `MIN_PRICE` | DOUBLE |  |  | This column represents the minimum price that an item can be regardless of any algorithms applied to calculate price. |
| 17 | `OPERATING_MARGIN_PCT` | DOUBLE | NOT NULL |  | This column in longer used |
| 18 | `PHARM_IND` | DOUBLE | NOT NULL |  | Indicates if this record is a pharmacy price schedule. |
| 19 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the pharmacy domain related to the Price Schedule. The Price Schedule is tailored to a Retail Pharmacy's specific needs to calculate the price of a prescription. |
| 20 | `PRICE_SCHED_DESC` | VARCHAR(200) |  |  | The description given to the price schedule. |
| 21 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the price_sched table. It is an internal system assigned number. |
| 22 | `PRICE_SCHED_SHORT_DESC` | VARCHAR(50) |  |  | The short description given to the price schedule. |
| 23 | `RANGE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of range for the FROM and TO parameters on the Price Range table. This includes COST, QTY and DAYS SUPPLY. |
| 24 | `ROUNDING_RATE_FLAG` | DOUBLE | NOT NULL |  | Per price schedule to round up/down/standard |
| 25 | `ROUND_UP` | DOUBLE |  |  | This column represents a value to be applied towards the price based on defined rounding methods. |
| 26 | `SELF_PAY_IND` | DOUBLE | NOT NULL |  | The self pay indicator identifies if the bill is the patient's responsibility or not. |
| 27 | `STANDARD_SCHED_IND` | DOUBLE |  |  | Indicates whether or not the price schedule is the standard price schedule for the related organization. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `WARNING_DT_TM` | DATETIME |  |  | The warning date and time specified when the price schedule was created. |
| 34 | `WARNING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that specified the warning date, time and type code for this price schedule. |
| 35 | `WARNING_TYPE_CD` | DOUBLE | NOT NULL |  | The code value from 13032 indicating the mechnism by which a warning will be issued. Options include telephone and send email. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WARNING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (15)

| From table | Column |
|------------|--------|
| [CHARGE](CHARGE.md) | `LIST_PRICE_SCHED_ID` |
| [CHARGE](CHARGE.md) | `PRICE_SCHED_ID` |
| [DISPENSE_CATEGORY](DISPENSE_CATEGORY.md) | `PRICE_SCHED_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `PRICE_SCHED_ID` |
| [MED_OE_DEFAULTS](MED_OE_DEFAULTS.md) | `PRICE_SCHED_ID` |
| [MM_CS_PATIENT_PRICE](MM_CS_PATIENT_PRICE.md) | `PRICE_SCHED_ID` |
| [MM_PRICE_FORMULA](MM_PRICE_FORMULA.md) | `PRICE_SCHED_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `PRICE_SCHEDULE_ID` |
| [PRICE_CODE_EXCEPTION](PRICE_CODE_EXCEPTION.md) | `COPAY_PRICE_SCHED_ID` |
| [PRICE_CODE_EXCEPTION](PRICE_CODE_EXCEPTION.md) | `PRICE_SCHED_ID` |
| [PRICE_RANGE](PRICE_RANGE.md) | `PRICE_SCHED_ID` |
| [PRICE_SCHED_ITEMS](PRICE_SCHED_ITEMS.md) | `PRICE_SCHED_ID` |
| [PRICE_SCHED_ITEMS_HIST](PRICE_SCHED_ITEMS_HIST.md) | `PRICE_SCHED_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `PRICE_SCHED_ID` |
| [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `PRICE_SCHED_ID` |

