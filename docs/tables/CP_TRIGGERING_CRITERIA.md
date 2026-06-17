# CP_TRIGGERING_CRITERIA

> Contains the triggering criteria associated to a Care Pathway ( Care Planning MPAGE)

**Description:** Care Planning Triggering Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CP_PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key for the CP_PATHWAY table. |
| 2 | `CP_TRIGGERING_CRITERIA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `CRITERIA_TYPE_MEAN` | VARCHAR(100) | NOT NULL |  | Identifies different types of triggring criteria. Examples of values are DIAGNOSIS_FAMILY and REASON_FOR_VISIT |
| 4 | `TRIGGERING_CRITERIA_GROUP_MEAN` | VARCHAR(255) | NOT NULL |  | Stores the meaning for the triggering criteria group |
| 5 | `TRIGGERING_CRITERIA_IDENT` | VARCHAR(255) |  |  | Optional identifier for table. Used instead of TRIGGERING_ENTITY_ID and TRIGGERING_ENTITY_NAME - and contains a CKI value from CMT_CONCEPT. |
| 6 | `TRIGGERING_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key for the table identified by TRIGGERING_ENTITY_NAME. |
| 7 | `TRIGGERING_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies a table used to identify triggering criteria (ie, NOMENCLATURE) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_PATHWAY_ID` | [CP_PATHWAY](CP_PATHWAY.md) | `CP_PATHWAY_ID` |

