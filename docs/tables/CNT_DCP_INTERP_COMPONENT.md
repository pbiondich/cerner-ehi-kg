# CNT_DCP_INTERP_COMPONENT

> CONTENCT DCP INTERPRET COMPONENTS

**Description:** CNT DCP INTERP COMPONENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_DCP_INTERP_COMPONENT_ID` | DOUBLE | NOT NULL |  | Sequence generated ID - PRIMARY KEY |
| 2 | `CNT_DCP_INTERP_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID |
| 3 | `COMPONENT_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 4 | `COMPONENT_SEQUENCE` | DOUBLE | NOT NULL |  | sequence number of the component. |
| 5 | `DCP_INTERP_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Interp |
| 6 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | description of component. |
| 7 | `FLAGS` | DOUBLE | NOT NULL |  | flags which identify properties of the component 1 - numeric component |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DCP_INTERP_ID` | [CNT_DCP_INTERP2](CNT_DCP_INTERP2.md) | `CNT_DCP_INTERP2_ID` |

