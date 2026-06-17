# CDI_AC_BATCHMODULE

> The CDI Ascent Capture Batch Module table

**Description:** CDI Ascent Capture Batch Module  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCHDESCRIPTION` | VARCHAR(80) | NOT NULL |  | batch description |
| 2 | `BATCHMODULEID` | VARCHAR(38) | NOT NULL |  | batch module identifier |
| 3 | `BATCHSTATUS` | DOUBLE |  |  | batch status |
| 4 | `CDI_AC_BATCHMODULE_ID` | DOUBLE | NOT NULL |  | cdi ascent capture batch module identifier |
| 5 | `CDI_AC_BATCH_ID` | DOUBLE | NOT NULL | FK→ | cdi ascent capture batch identifier column |
| 6 | `CHANGEDFORMTYPES` | DOUBLE |  |  | changed form types |
| 7 | `DELETED` | DOUBLE |  |  | deleted |
| 8 | `DOCUMENTSCREATED` | DOUBLE |  |  | documents created |
| 9 | `DOCUMENTSDELETED` | DOUBLE |  |  | documents deleted |
| 10 | `ENDDATETIME` | DATETIME | NOT NULL |  | end date time |
| 11 | `ERRORCODE` | DOUBLE |  |  | error code |
| 12 | `ERRORTEXT` | VARCHAR(255) | NOT NULL |  | error text |
| 13 | `EXPECTEDDOCS` | DOUBLE |  |  | expected docs |
| 14 | `EXPECTEDPAGES` | DOUBLE |  |  | expected pages |
| 15 | `EXTERNAL_BATCH_IDENT` | DOUBLE | NOT NULL |  | external batch identifier value |
| 16 | `MODULECLOSEUNIQUEID` | VARCHAR(250) | NOT NULL |  | module close unique identifier |
| 17 | `MODULELAUNCHID` | VARCHAR(38) | NOT NULL |  | module launch identifier |
| 18 | `MODULENAME` | VARCHAR(32) | NOT NULL |  | module name |
| 19 | `ORPHANED` | DOUBLE |  |  | orphaned |
| 20 | `PAGESDELETED` | DOUBLE |  |  | PAGES DELETED |
| 21 | `PAGESPERDOCUMENT` | DOUBLE |  |  | pages per document |
| 22 | `PAGESREPLACED` | DOUBLE |  |  | pages replaced |
| 23 | `PAGESSCANNED` | DOUBLE |  |  | pages scanned |
| 24 | `PRIORITY` | DOUBLE |  |  | priority value |
| 25 | `STARTDATETIME` | DATETIME |  |  | start date and time |
| 26 | `TRANSFERID` | VARCHAR(38) | NOT NULL |  | transfer identifier |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_AC_BATCH_ID` | [CDI_AC_BATCH](CDI_AC_BATCH.md) | `CDI_AC_BATCH_ID` |

