# PROV_PATDEMO_ENTITY

> Stores information about entities associated to the provenance PATIENT DEMOGRAPHICS concept

**Description:** PROV_PATDEMO_ENTITY  
**Table type:** ACTIVITY  
**Primary key:** `PROV_PATDEMO_ENTITY_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ENTITY_ROLE_CD` | DOUBLE | NOT NULL |  | Code value describing the entity role in the provenance activity - e.g. SOURCE. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Pk for the entity table identified in field PARENT_ENTITY_NAME. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Entity table name - e.g. SI_DOCUMENT_METADATA - PERSON |
| 6 | `PROVENANCE_PATDEMO_ID` | DOUBLE | NOT NULL | FK→ | Pk for the Provenance_PATDEMO table. |
| 7 | `PROV_PATDEMO_ENTITY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROVENANCE_PATDEMO_ID` | [PROVENANCE_PATDEMO](PROVENANCE_PATDEMO.md) | `PROVENANCE_PATDEMO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROV_PATDEMO_ENTY_PRTCPNT](PROV_PATDEMO_ENTY_PRTCPNT.md) | `PROV_PATDEMO_ENTITY_ID` |

