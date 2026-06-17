# SI_HAAD_FILE_POLL

> HAAD Search Transaction Poll Log

**Description:** SI HAAD File Poll  
**Table type:** ACTIVITY  
**Primary key:** `SI_HAAD_FILE_POLL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | Time at which polling ended |
| 2 | `POLL_COUNT` | DOUBLE | NOT NULL |  | Number of the times the search transaction was called for a given poll |
| 3 | `POLL_TYPE_BIT` | DOUBLE | NOT NULL |  | This field will contain a bit map value to correspond to various options/combinations |
| 4 | `SENDING_FACILITY_IDENT` | VARCHAR(75) | NOT NULL |  | HAAD license number of sending facility |
| 5 | `SI_HAAD_FILE_POLL_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `START_DT_TM` | DATETIME | NOT NULL |  | Time at which polling began |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_HAAD_FILE_DOWNLOAD](SI_HAAD_FILE_DOWNLOAD.md) | `SI_HAAD_FILE_POLL_ID` |

