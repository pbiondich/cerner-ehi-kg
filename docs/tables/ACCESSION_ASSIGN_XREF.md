# ACCESSION_ASSIGN_XREF

> This table associates accession formats with an assignment bucket.

**Description:** Accession Assignment Cross Reference  
**Table type:** REFERENCE  
**Primary key:** `ACCESSION_FORMAT_CD`, `SITE_PREFIX_CD`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ASSIGNMENT_POOL_ID` | DOUBLE | NOT NULL | FK→ | A system generated number that uniquely identifies an accession assignment bucket. |
| 2 | `ACCESSION_FORMAT_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system as a code value for the Accession Format. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (PathNet, RadNet) and/or what department (General Lab, Microbiology) an order belongs. |
| 4 | `SITE_PREFIX_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system as a code value for the Site Prefix of an accession number. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ASSIGNMENT_POOL_ID` | [ACCESSION_ASSIGN_POOL](ACCESSION_ASSIGN_POOL.md) | `ACCESSION_ASSIGNMENT_POOL_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_PREFIX](AP_PREFIX.md) | `ACCESSION_FORMAT_CD` |
| [AP_PREFIX](AP_PREFIX.md) | `SITE_CD` |

