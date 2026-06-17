# DD_CONTRIBUTION

> Represents a contribution to a document. The contribution can have a single unique session (i.e. lock) and groups multiple sections in DD_SECTION.

**Description:** Dynamic Documentation Contribution  
**Table type:** ACTIVITY  
**Primary key:** `DD_CONTRIBUTION_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the author of the document |
| 2 | `DD_CONTRIBUTION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a contribution to a document. |
| 3 | `DOC_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related clinical event, doc, to which this contribution is associated. Note that the DOC links to the document text. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter. Patient level documents have an encounter ID of 0. |
| 5 | `MDOC_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related clinical event to which the MDOC this contribution is associated. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient associated to the document. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_EMR_EXTRACT](DD_EMR_EXTRACT.md) | `DD_CONTRIBUTION_ID` |

