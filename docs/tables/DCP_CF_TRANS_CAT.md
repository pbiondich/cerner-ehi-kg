# DCP_CF_TRANS_CAT

> The purpose of the table is to hold the reference content that will used tor transfer the clinical facts from a patient A to Patient B during pregnancy, organ donation and so on.

**Description:** Clinical Facts transfer categories  
**Table type:** REFERENCE  
**Primary key:** `DCP_CF_TRANS_CAT_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CF_CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the category as defined by the user for which the transfer of data is going to happen. |
| 4 | `CF_TRANSFER_TYPE_CD` | DOUBLE | NOT NULL |  | Describe for what Transfer_type they are going to use the category for. Code_set : 7000 will define transfer_type_cd |
| 5 | `DCP_CF_TRANS_CAT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the table |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DCP_CF_TRANS_CAT_RELTN](DCP_CF_TRANS_CAT_RELTN.md) | `DCP_CF_TRANS_CAT_ID` |

