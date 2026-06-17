# SCH_CAB_RES

> This table is used for defining resources for choose and book services

**Description:** Scheduling CAB resources  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAB_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduling Choose and Book Service. |
| 2 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 3 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The display order of the object within the collection. |
| 4 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | The identifier for the resource. A resource is an item of limited availability. |
| 5 | `ROLE_PROFILE` | VARCHAR(255) | NOT NULL |  | the role profile |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CAB_SERVICE_ID` | [SCH_CAB_SERVICE](SCH_CAB_SERVICE.md) | `CAB_SERVICE_ID` |

