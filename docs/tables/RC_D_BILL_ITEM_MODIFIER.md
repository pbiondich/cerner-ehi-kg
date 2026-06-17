# RC_D_BILL_ITEM_MODIFIER

> Stores modifiers in a specific order for each bill code from data captured by GSR Revenue Extract

**Description:** Revenue Cycle Dimension Bill Item Modifier  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BILL_ITEM_MODIFIER_ID`  
**Columns:** 20  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `PRIMARY_MODIFIER` | VARCHAR(50) |  |  | This is the first modifier associated to a bill item. |
| 10 | `QUATERNARY_MODIFIER` | VARCHAR(50) |  |  | This is the fourth modifier associated to a bill item. |
| 11 | `RC_D_BILL_ITEM_MODIFIER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_D_BILL_ITEM_MODIFIER table. |
| 12 | `SECONDARY_MODIFIER` | VARCHAR(50) |  |  | The second modifier associated to a bill item. |
| 13 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | CODE SET:400 The external vocabulary or lexicon that contributed the string, e.g. CPT, HCPCS, etc. |
| 14 | `SOURCE_VOCABULARY_TEXT` | VARCHAR(40) |  |  | Stores the display of the source_vocabulary_cd. |
| 15 | `TERTIARY_MODIFIER` | VARCHAR(50) |  |  | The third modifier associated to a bill_item. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_CPT_MODIFIER_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_HCPCS_MODIFIER_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_CPT_MODIFIER_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_HCPCS_MODIFIER_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_CPT_MODIFIER_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_HCPCS_MODIFIER_ID` |

