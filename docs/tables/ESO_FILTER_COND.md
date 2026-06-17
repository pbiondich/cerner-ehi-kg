# ESO_FILTER_COND

> ESO filter cond Table

**Description:** ESO filter cond  
**Table type:** REFERENCE  
**Primary key:** `FILTER_COND_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date that the record was created in the table. |
| 5 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | This string provides a description of the event trigger row. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FILTER_COND_CD` | DOUBLE | NOT NULL |  | filter cond codeColumn |
| 8 | `FILTER_COND_ID` | DOUBLE | NOT NULL | PK | filter condition identifierColumn |
| 9 | `FILTER_COND_VALUE` | VARCHAR(255) |  |  | filter cond valueColumn |
| 10 | `ORIGINAL_FILTER_COND_IDENT` | DOUBLE | NOT NULL |  | original filter cond identifierColumn |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ESO_FILTER_COND_RELTN](ESO_FILTER_COND_RELTN.md) | `FILTER_COND_ID` |

