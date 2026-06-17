# DO_MAPPING_NOMENCLATURE

> Discern Ontology Nomenclature Mappings

**Description:** DO_MAPPING_NOMENCLATURE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_CODE` | VARCHAR(100) |  |  | Code from the code system. |
| 2 | `DO_CODE_SYSTEM_URI` | VARCHAR(200) |  |  | URI of the code system. |
| 3 | `DO_MAPPING_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_MAPPING_NOMENCLATURE table. |
| 4 | `DO_MAPPING_SEQ` | DOUBLE | NOT NULL |  | Global sequence of the mapping. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the NOMENCLATURE table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

