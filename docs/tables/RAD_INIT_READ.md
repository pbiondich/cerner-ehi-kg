# RAD_INIT_READ

> The contents of RAD_INIT_READ allows for the system tracking of information, that formerly existed as yellow sticky notes on the Film or in the Film folder, created by an ED Physician to be associated with an acquired study from a modality. The table also tracks the later entry by a Radiologist that may indicate a different finding or agree/disagree with the ED Physician's initial read.

**Description:** Radiology Initial Reading  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | This column contains the type of user-performed activity. |
| 2 | `CONSULTATION_CD` | DOUBLE | NOT NULL |  | This column identifies the consultation required. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order ID for which the wet read is being stored. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This column contains the unique ID of a foreign table such as Acquired Study ID, Accession_ID |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This column contains the name of the table where the Parent_Entity_ID comes from. EX: IM_Acquired_Study or ORDER_RADIOLOGY table |
| 6 | `RAD_INIT_READ_ID` | DOUBLE | NOT NULL |  | This column contains a unique number that serves the purpose of uniquely identifying a wet read. |
| 7 | `READ_BY_DT_NBR` | DOUBLE | NOT NULL |  | Date Number used for calculation of other date related dimensions and filters for an initial read. |
| 8 | `READ_BY_DT_TM` | DATETIME |  |  | Date and time the row was added. |
| 9 | `READ_BY_ID` | DOUBLE | NOT NULL | FK→ | Person ID of the person adding the wet read row. |
| 10 | `READ_BY_MIN_NBR` | DOUBLE | NOT NULL |  | Minute value used for calculation of other time related dimensions and filters indicating when the initial read was created. |
| 11 | `READ_BY_TZ` | DOUBLE |  |  | Time zone associated with the column READ_BY_DT_TM. |
| 12 | `READ_TEXT` | VARCHAR(255) |  |  | This column contains the text string for initial reading. It identifies the text entered during wet read. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `READ_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

