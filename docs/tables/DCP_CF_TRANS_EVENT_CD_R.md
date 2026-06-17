# DCP_CF_TRANS_EVENT_CD_R

> The purpose of the table is to hold the reference content that will relate source and target event code based on transfer_type and related indentifier that is needed to move the data

**Description:** Clinical Facts transfer categories  
**Table type:** REFERENCE  
**Primary key:** `DCP_CF_TRANS_EVENT_CD_R_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOCIATION_IDENTIFIER_CD` | DOUBLE | NOT NULL |  | This is unique identifier that will define either fetus/baby identifier or organ identifier. This will zero if the data need moved for all identifier. Code set:6999. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CF_TRANSFER_TYPE_CD` | DOUBLE | NOT NULL |  | This will specify the reason for moving the data from target to source domain. Possible reasons for transferring specified in the code_set:7000 |
| 5 | `DCP_CF_TRANS_EVENT_CD_R_ID` | DOUBLE | NOT NULL | PK | To have Primary key/unique identifier on the table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `SOURCE_EVENT_CD` | DOUBLE | NOT NULL |  | From code_set:72. This is the event_cd that's when results are documented, since target is not established. |
| 8 | `TARGET_EVENT_CD` | DOUBLE | NOT NULL |  | This is the event_cd is where the results are going to transfer to on targets record. From code_set:72. This is the event_cd that's when results are going to be transfer to target_cd |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DCP_CF_TRANS_CAT_RELTN](DCP_CF_TRANS_CAT_RELTN.md) | `DCP_CF_TRANS_EVENT_CD_R_ID` |

