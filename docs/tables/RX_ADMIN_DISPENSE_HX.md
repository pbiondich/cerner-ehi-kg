# RX_ADMIN_DISPENSE_HX

> Stores the historical pharmacy information related to the administrations associated with a dispense event.

**Description:** Pharmacy Administration Dispense History  
**Table type:** ACTIVITY  
**Primary key:** `RX_ADMIN_DISPENSE_HX_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_DT_TM` | DATETIME |  |  | The date and time of the administration that has been dispensed. |
| 2 | `ADMIN_TOTAL_PRICE_AMT` | DOUBLE | NOT NULL |  | The total price for this dispensed administration. |
| 3 | `ADMIN_TZ` | DOUBLE | NOT NULL |  | The time zone associated with the administration date and time. |
| 4 | `CHARGE_DT_TM` | DATETIME |  |  | The date and time at which the administration was charged to the patient. |
| 5 | `CHARGE_FLAG` | DOUBLE | NOT NULL |  | Indicates the charge status of the administration. |
| 6 | `CHARGE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the charge date and time. |
| 7 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the dispense event to which this administration dispense is associated. |
| 8 | `DOSE_AMT` | DOUBLE | NOT NULL |  | The number of doses that are dispensed or credited for this administration. |
| 9 | `REF_RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a reference administration dispense to this administration dispense. |
| 10 | `RESIDUAL_DOSE_AMT` | DOUBLE | NOT NULL |  | The number of doses remaining after a reverse has occurred. |
| 11 | `RESIDUAL_PRICE_AMT` | DOUBLE | NOT NULL |  | The price to be charged after a reverse has occurred. (Original price less credited price) |
| 12 | `REVERSE_IND` | DOUBLE | NOT NULL |  | Indicates that this administration dispense charge has been reversed. |
| 13 | `REV_RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the admin dispense history row that is being reversed by this entry. |
| 14 | `RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_ADMIN_DISPENSE_HX table. |
| 15 | `SUPPRESS_CHARGE_FLAG` | DOUBLE |  |  | Indicates whether the charges have been suppressed for the inpatient dispense |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `REF_RX_ADMIN_DISPENSE_HX_ID` | [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |
| `REV_RX_ADMIN_DISPENSE_HX_ID` | [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `RX_ADMIN_DISPENSE_HX_ID` |
| [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `REF_RX_ADMIN_DISPENSE_HX_ID` |
| [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `REV_RX_ADMIN_DISPENSE_HX_ID` |
| [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |

