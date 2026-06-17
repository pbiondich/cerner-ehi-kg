# RR_ACCESSION_R

> Stores information about the round robin accessions generated

**Description:** Round Robin Accession Relation  
**Table type:** ACTIVITY  
**Primary key:** `ACCESSION_ID`, `ROUND_ROBIN_REF_ID`  
**Columns:** 8  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | PK FK→ | A unique, internal, system-assigned number that identifies a specific accession number associated with a round robin template. Creates a relationship to the accession table. |
| 2 | `ROUND_ROBIN_REF_ID` | DOUBLE | NOT NULL | PK FK→ | A unique, internal, system-assigned number that identifies a specific round robin template. |
| 3 | `RR_GROUP_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a grouping of a set of accessions that were created at the same time. Creates a relationship to the round robin group table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `ROUND_ROBIN_REF_ID` | [ROUND_ROBIN_REF](ROUND_ROBIN_REF.md) | `ROUND_ROBIN_REF_ID` |
| `RR_GROUP_ID` | [RR_GROUP](RR_GROUP.md) | `RR_GROUP_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ROUND_ROBIN_COMMENT](ROUND_ROBIN_COMMENT.md) | `ACCESSION_ID` |
| [ROUND_ROBIN_COMMENT](ROUND_ROBIN_COMMENT.md) | `ROUND_ROBIN_REF_ID` |
| [RR_RESULT](RR_RESULT.md) | `ACCESSION_ID` |
| [RR_RESULT](RR_RESULT.md) | `ROUND_ROBIN_REF_ID` |

