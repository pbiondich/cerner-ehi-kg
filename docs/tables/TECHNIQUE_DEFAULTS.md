# TECHNIQUE_DEFAULTS

> This table sets up the relationships between a catalog_cd, department_cd and exam_room_cd for default technique fields.

**Description:** Radiology Technique Defaults  
**Table type:** REFERENCE  
**Primary key:** `TECHNIQUE_DEFAULT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog_cd is a foreign key to the order_catalog table. It uniquely identifies the procedure that the defaults are set up for. |
| 2 | `DEPARTMENT_CD` | DOUBLE | NOT NULL | FK→ | The department_cd is a foreign key to the service_resource table. It uniquely identifies the department that is having the defaults set up for. |
| 3 | `EXAM_ROOM_CD` | DOUBLE | NOT NULL | FK→ | The Exam_Room_Cd is a foreign key to the service_resource table. It uniquely identifies the exam room that is having defaults set up for. |
| 4 | `SEQUENCE` | DOUBLE |  |  | This column identifies the sequence in which the defaults should appear in Exam Mgmt. |
| 5 | `TECHNIQUE_DEFAULT_ID` | DOUBLE | NOT NULL | PK | This column is a meaningless number that only serves as a unique identifier for the row. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `DEPARTMENT_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `EXAM_ROOM_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TECHNIQUE_DEFAULT_VALS](TECHNIQUE_DEFAULT_VALS.md) | `TECHNIQUE_DEFAULT_ID` |

