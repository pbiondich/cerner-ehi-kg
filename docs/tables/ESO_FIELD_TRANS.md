# ESO_FIELD_TRANS

> ESO field trans

**Description:** ESO Field Trans  
**Table type:** REFERENCE  
**Primary key:** `FIELD_TRANS_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | create date and timeColumn |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIELD_CD` | DOUBLE | NOT NULL |  | field codeColumn |
| 7 | `FIELD_TRANS_ID` | DOUBLE | NOT NULL | PK | field trans identifierColumn |
| 8 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | field type codeColumn |
| 9 | `GROUP_CD` | DOUBLE | NOT NULL |  | group codeColumn |
| 10 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | message format codeColumn |
| 11 | `MESSAGE_TRIGGER_CD` | DOUBLE | NOT NULL |  | message trigger codeColumn |
| 12 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL |  | message type codeColumn |
| 13 | `MESSAGE_VERSION_CD` | DOUBLE | NOT NULL |  | message version codeColumn |
| 14 | `ORIGINAL_FIELD_TRANS_IDENT` | DOUBLE | NOT NULL |  | original field trans identifierColumn |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ESO_FIELD_FILTER_RELTN](ESO_FIELD_FILTER_RELTN.md) | `FIELD_TRANS_ID` |

