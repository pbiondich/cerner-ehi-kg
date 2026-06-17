# SIGN_LINE_DTA_R

> This table contains the relationships between the discrete task assay (and/or activity sub-type) with the signature line format code.

**Description:** Signature Line - Discrete Task Assay Relationships  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | This field stores the activity sub-type code, if defined, to which a signature line format can be defined. Association of a signature line format to an activity sub-type is more generic than when associated to an actual discrete task assay. |
| 2 | `FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identication code representing the signature line format. This value is used to join to the signature line format information stored on the SIGN_LINE_FORMAT table. |
| 3 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | This field contains a flag value representing the result status for which the signature line format is associated. Optionally, signature lines can be associated with "performed and verified" results, only "performed" results, or only "verified" results. |
| 4 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field stores the discrete task assay identification code, if defined, to which a signature line format is assigned. Association of a signature line format to a discrete task assay is more specific than assigning a format to an activity sub-type value. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORMAT_ID` | [SIGN_LINE_FORMAT](SIGN_LINE_FORMAT.md) | `FORMAT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

