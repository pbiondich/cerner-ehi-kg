# PROVENANCE_GEN_LAB

> Stores provenance information for the GEN LAB concept

**Description:** Provenance for GEN LAB  
**Table type:** ACTIVITY  
**Primary key:** `PROVENANCE_GEN_LAB_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `CLIENT_IDENT` | VARCHAR(100) |  |  | Unique identifier of the calling application. |
| 4 | `GROUP_ID` | DOUBLE | NOT NULL |  | This is a group identifier. It is the value of the PK of the first row in the group. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | PK on the Concept table identified in PARENT_ENTITY_NAME |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Concept Table Name ( CLINICAL_EVENT - GEN_LAB_EXT_DATA) |
| 7 | `PERSONA_TXT` | VARCHAR(40) | NOT NULL |  | Identifies the user's persona, e.g. PATIENT, PERSONNEL, SYSTEM. |
| 8 | `PROVENANCE_GEN_LAB_ID` | DOUBLE | NOT NULL | PK | THE PRIMARY KEY |
| 9 | `PROVENANCE_RECORDED_DT_TM` | DATETIME | NOT NULL |  | The Date that the Provenance data was written into Millennium. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PROV_GEN_LAB_ENTITY](PROV_GEN_LAB_ENTITY.md) | `PROVENANCE_GEN_LAB_ID` |
| [PROV_GEN_LAB_PARTICIPANT](PROV_GEN_LAB_PARTICIPANT.md) | `PROVENANCE_GEN_LAB_ID` |

