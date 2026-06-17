# MIC_STAT_PROCESS

> This statistical table contains the begin and end ranges that the existing data will need to be archived.

**Description:** Micro Statistical Processing  
**Table type:** ACTIVITY  
**Primary key:** `PROCESS_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | This field indicates the beginning date of the time range. The complete date of the culture will be used to determine if the procedure falls within the date range. |
| 2 | `COMPLETE_IND` | DOUBLE |  |  | This field indicator whether data has been archived for the specified date range. |
| 3 | `END_DT_TM` | DATETIME | NOT NULL |  | This field indicates the ending date of the time range. The complete date of the culture will be used to determine if the procedure falls within the date range. |
| 4 | `PROCESS_ID` | DOUBLE | NOT NULL | PK | This field contains a unique value that identifies all the procedures falls into the defined time range. This value is used to join to mic_stat_archive and mic_stat_duplicate tables. |
| 5 | `PROCESS_TECH_ID` | DOUBLE | NOT NULL | FK→ | This field indicates the tech that archived the data. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROCESS_TECH_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_STAT_ARCHIVE](MIC_STAT_ARCHIVE.md) | `PROCESS_ID` |
| [MIC_STAT_DUPLICATE](MIC_STAT_DUPLICATE.md) | `PROCESS_ID` |

