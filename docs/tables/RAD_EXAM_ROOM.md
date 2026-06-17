# RAD_EXAM_ROOM

> The Rad_Exam_Room table is a child of the service_resource table and contains information specific to the exam rooms where radiology procedures are performed.

**Description:** Rad Exam Room  
**Table type:** REFERENCE  
**Primary key:** `SERVICE_RESOURCE_CD`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MPPS_RESET_IND` | DOUBLE | NOT NULL |  | This field indicates whether the system will allow MPPS to reset procedures. |
| 2 | `MPPS_START_IND` | DOUBLE | NOT NULL |  | This field indicates whether the system will allow MPPS to start procedures performed in this room. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The Service_Resource_Cd is a foreign key to the Service_Resource table. It uniquely identifies the exam room. |
| 4 | `TEMP_MULTI_FLAG` | DOUBLE |  |  | The Temp_Multi_Flag indicates if temporary tracking of multi day studies are being done within the exam room. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXAM_ROOM_LIB_GRP_RELTN](EXAM_ROOM_LIB_GRP_RELTN.md) | `SERVICE_RESOURCE_CD` |

