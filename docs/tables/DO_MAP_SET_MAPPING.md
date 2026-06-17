# DO_MAP_SET_MAPPING

> Defines the code/identifier mappings between two different valuesets.

**Description:** Discern Ontology Map Valuesets Mappings  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_MAPPING_VERSION` | DOUBLE | NOT NULL |  | The Cloud Version Number for the mapping entry. This is used to synchronize data between the cloud and the Millennium Databases. |
| 2 | `DO_MAP_SET_ID` | DOUBLE | NOT NULL | FK→ | This number ties the mapping back to a row in the DO_MAP_SET DB Table. It lets you what set the identifier comes from. |
| 3 | `DO_MAP_SET_MAPPING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_MAP_SET_MAPPING table. |
| 4 | `DO_SOURCE_IDENTIFIER` | VARCHAR(512) | NOT NULL |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies an Cerner or industry idenfier for a code within a value set. |
| 5 | `DO_SOURCE_NAMESPACE` | VARCHAR(128) | NOT NULL |  | "Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies a well known identifier for the valueset (ex. FHIR code representing the set).; this uniquely identifies a single row in the VOCABULARIES or CODE_SYSTEMS table." |
| 6 | `DO_TARGET_DISPLAY` | VARCHAR(2048) |  |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this column contains the display name of the CONCEPT or IDENTITY_CODE. |
| 7 | `DO_TARGET_IDENTIFIER` | VARCHAR(512) | NOT NULL |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies an Cerner or industry idenfier for the item being mapped. |
| 8 | `DO_TARGET_NAMESPACE` | VARCHAR(128) | NOT NULL |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies a well known identifier for the valueset (ex. FHIR code representing the set).; Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies a single row in the VOCABULARIES or CODE_SYSTEMS table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_MAP_SET_ID` | [DO_MAP_SET](DO_MAP_SET.md) | `DO_MAP_SET_ID` |

