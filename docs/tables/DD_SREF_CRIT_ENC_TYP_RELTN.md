# DD_SREF_CRIT_ENC_TYP_RELTN

> Relation table which links a particular chief complaint criteria row to one or more structured documentation reference templates.

**Description:** Dynamic Documenation Structured Documenation Criteria Encounter Type Relationshi  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_SREF_CHF_CMPLNT_CRIT_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the chief complaint criteria entry which is linked to one or more encounter types. |
| 2 | `DD_SREF_CRIT_ENC_TYP_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between a chief complaint criteria and a related encounter type. |
| 3 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type class or encounter type which should be linked to a particular chief complaint criteria entry. Values come from codeset 71 or codeset 69. A value of 0.0 indicates the criteria is valid for all encounter types. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SREF_CHF_CMPLNT_CRIT_ID` | [DD_SREF_CHF_CMPLNT_CRIT](DD_SREF_CHF_CMPLNT_CRIT.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |

