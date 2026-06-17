# RC_D_BILL_PROPERTY

> Contains the data associated to claim attributes for reporting purposes.

**Description:** Revenue Cycle Dimension Bill Property  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BILL_PROPERTY_ID`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILL_STATUS` | VARCHAR(40) |  |  | Contains all the statuses for a claim. (ex: pending, ready to bill, etc.) |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `MEDIA_SUB_TYPE` | VARCHAR(40) |  |  | Identifies the media sub type of claim. (ex: cms1500, etc.:) |
| 8 | `MEDIA_TYPE` | VARCHAR(40) |  |  | Identifies the media type of claim. (ex: edi, paper, etc.:) |
| 9 | `MILL_BILL_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the bill status code on the Millennium table from which this row was derived. |
| 10 | `MILL_MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the media sub type code on the millennium table from which this row was derived. |
| 11 | `MILL_MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the media type of claim (ex: edi, paper, etc.) |
| 12 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data associated to claim attributes for reporting purposes. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_BILL_PROPERTY_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_BILL_PROPERTY_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_BILL_PROPERTY_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_BILL_PROPERTY_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_BILL_PROPERTY_ID` |

