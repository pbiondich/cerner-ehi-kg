# MLTM_INT_HEADER_SEVERITY_MAP

> Multum INT_HEADER_SEVERITY_MAP table

**Description:** MLTM INT Header Severity Map  
**Table type:** REFERENCE  
**Primary key:** `HEADER_ID`, `SEVERITY_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HEADER_ID` | DOUBLE | NOT NULL | PK FK→ | Header ID - 1st column in 2-column PK. FK from table MLTM_INT_HEADER |
| 2 | `SEQUENCE_NUMBER` | DOUBLE | NOT NULL |  | Sequence Number |
| 3 | `SEVERITY_ID` | DOUBLE | NOT NULL | PK FK→ | Severity ID - 2nd column of 2-column PK. FK from MLTM_SEVERITY |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEADER_ID` | [MLTM_INT_HEADER](MLTM_INT_HEADER.md) | `HEADER_ID` |
| `SEVERITY_ID` | [MLTM_SEVERITY](MLTM_SEVERITY.md) | `SEVERITY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLTM_INT_INTERACT_SEVERITY_MAP](MLTM_INT_INTERACT_SEVERITY_MAP.md) | `HEADER_ID` |
| [MLTM_INT_INTERACT_SEVERITY_MAP](MLTM_INT_INTERACT_SEVERITY_MAP.md) | `SEVERITY_ID` |

