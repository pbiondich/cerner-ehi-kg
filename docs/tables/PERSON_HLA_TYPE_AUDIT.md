# PERSON_HLA_TYPE_AUDIT

> Provides an audit trail of the Person HLA Type table whenever a record is modified.

**Description:** Person HLA Type Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_DT_TM` | DATETIME |  |  | Date and time that the audit record was created. |
| 2 | `CHARTED_IND` | DOUBLE |  |  | Indicator to signify whether the row has been charted. |
| 3 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where HLA Typing history audit trail comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 4 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA Typing results were completed. |
| 5 | `HLA_DT_TM` | DATETIME |  |  | Date and time that the original person_hla_type record was created. |
| 6 | `HLA_TYPE_AUDIT_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an HLA Typing History audit record. |
| 7 | `HLA_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Relates this audit record to the current HLA Typing History record. It is a foreign key reference to the primary key of the person_hla_type table. |
| 8 | `HLA_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the antigen which is part of the HLA Typing. |
| 9 | `LOCI_CD` | DOUBLE | NOT NULL |  | The code for the specific HLA Loci where the HLA antigen is located. |
| 10 | `OUTSIDE_TYPING_IND` | DOUBLE |  |  | Indicates that the HLA Typing was performed by an external laboratory. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the user who updated the person_hla_type record which resulted in the creation of this audit record. |
| 13 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the specimen type used for the hla typing. |
| 14 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Relates this HLA type to an associated procedure. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HLA_TYPE_ID` | [PERSON_HLA_TYPE](PERSON_HLA_TYPE.md) | `HLA_TYPE_ID` |
| `HLA_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

