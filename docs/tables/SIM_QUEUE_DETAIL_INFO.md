# SIM_QUEUE_DETAIL_INFO

> This table contains details for the Cerner defined Queue Detail options. It is related to the FSIESO_QUE_DETAIL->Parent_Entity_Name

**Description:** SIM Queue Detail Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_DISPLAY` | VARCHAR(60) | NOT NULL |  | This value is used if the Entity_Name is unclear in descriptive terms. Display this value to the user if populated. |
| 2 | `ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | This value ties to the PARENT_ENTITY_NAMEs on the FSIESO_QUE_DETAIL table. |
| 3 | `ENTITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | This value describes the type of values available for this Entity_Name. 0 - No Description 1 - Code Set 2 - ID |
| 4 | `ENTITY_TYPE_SOURCE_NBR` | DOUBLE | NOT NULL |  | This is the numerical value that describes the source of the Entity_Name. |
| 5 | `ENTITY_TYPE_SOURCE_TEXT` | VARCHAR(255) | NOT NULL |  | This is a textual description of the options available for the Entity_Name. Example - 'Person', 'Chart Trigger ID'. This can also hold delaminated values. |
| 6 | `OCCURRENCE_NBR` | DOUBLE | NOT NULL |  | This value is interpreted by the calling application to decide upon placement. This value is a binary enumerator. Each bit represents a specific section of the search. 0 means that the value is displayed everywhere. |
| 7 | `SIM_QUEUE_DETAIL_INFO_ID` | DOUBLE | NOT NULL |  | Primary key for this table. Value comes from ESO_SEQ sequence |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

