# PFT_CM_EVENT_LOG

> Contains transaction log entries for contract management changes.

**Description:** Profit Contract Management Event Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BILL_ITEM_GROUP2_ID` | DOUBLE | NOT NULL |  | Identifies the associated Bill Item "inclusion" Group |
| 6 | `BILL_ITEM_GROUP_ID` | DOUBLE | NOT NULL |  | Identifies the associated Bill Item "exclusion" Group |
| 7 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Associates the log record to the BO Health Plan |
| 8 | `DAYS_OF_SERVICE_CNT` | DOUBLE | NOT NULL |  | Days of service = admit_dt_tm - disch_dt_tm |
| 9 | `EXCLUDED_CHRG_AMT` | DOUBLE | NOT NULL |  | The total dollar amount of all charges in the excluded list |
| 10 | `MAX_PRICE_AMT` | DOUBLE | NOT NULL |  | The maximum price the package can have |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Associates the log record to its Nomenclature |
| 12 | `OUTLIER_COST_AMT` | DOUBLE | NOT NULL |  | The cost of the package for each day after the outlier days |
| 13 | `OUTLIER_DAYS_CNT` | DOUBLE | NOT NULL |  | The number of days the package is effective |
| 14 | `PFT_CM_EVENT_LOG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies each contract management event log |
| 15 | `PRICE_AMT` | DOUBLE | NOT NULL |  | The price of the package being coded |
| 16 | `TOTAL_CHRG_AMT` | DOUBLE | NOT NULL |  | The total dollar amount of all charges on the invoice |
| 17 | `TRANS_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Related alias for combination of trans_type_cd, trans_sub_type_cd and trans_reason_cd |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `TRANS_ALIAS_ID` | [PFT_TRANS_ALIAS](PFT_TRANS_ALIAS.md) | `PFT_TRANS_ALIAS_ID` |

