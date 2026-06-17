# TPL_APPL_DETAIL

> Stores the name of the application - like Stat-DX, Vital Images, etc. that use the build and launch application tool as well as the data necessary to launch them.

**Description:** Third Party Launch Application Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPL_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated ID for this table. |
| 3 | `APPL_TASK_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Corresponds to a row on the TPL_APPL_TASK_RELTN table. |
| 4 | `APPL_TYPE_FLAG` | DOUBLE | NOT NULL |  | Value determining whether application is a web address, an executable, or neither. |
| 5 | `CMD_PATH_TXT` | VARCHAR(512) |  |  | The path leading to the executable to be launched. In the event of a URL, points to the browser. |
| 6 | `CTX_PARAM_TXT` | VARCHAR(2048) |  |  | The context parameters that need to be passed in via command line or URL in the case of a web address. |
| 7 | `FILE_PATH_TXT` | VARCHAR(512) |  |  | The path to which a file will be created. |
| 8 | `FILE_TMPLT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | maps to the long text table. |
| 9 | `HTTP_POST_IND` | DOUBLE | NOT NULL |  | If this value is 1 and appl_type_flag is also 1, parameters will be hidden from user view via HTTP post protocol. |
| 10 | `RAD_SEND_LINKED_ACCN_IND` | DOUBLE | NOT NULL |  | Indicates if multiple multiple orders will share the same report data. 1 - send all accessions in the linked exam. 0 - Send only the selected accession in the linked exam. |
| 11 | `REUSE_PRCS_IND` | DOUBLE | NOT NULL |  | For a browser implementation this will (if allowed) try to reuse the active browser window. For an executable, it would set focus to the executable as opposed to launching another instance.0 - Start new process each time1 - Reuse the process if still active |
| 12 | `TEST_MODE_IND` | DOUBLE | NOT NULL |  | 0 - Inactive (default)1 - Active |
| 13 | `TITLE_TXT` | VARCHAR(255) | NOT NULL |  | The title that will appear in the front end application. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPL_TASK_RELTN_ID` | [TPL_APPL_TASK_RELTN](TPL_APPL_TASK_RELTN.md) | `APPL_TASK_RELTN_ID` |
| `FILE_TMPLT_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

