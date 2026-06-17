# MIC_ANG_DISQUAL

> This table contains information regarding coded responses that will cause a procedure to be disqualified from the automatic no growth reporting process.

**Description:** Microbiology Auto No Growth Disqaualify Codes  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value for each procedure/service resource/source combination assigned on the mic_ref_ang table for which automatic no growth reporting parameters and disqualifications are defined. |
| 2 | `DISQUAL_RESPONSES_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the negative coded report response or organism which if issued in a report should disqualify the procedure from the automatic no growth reporting process. |
| 3 | `DISQUAL_SEQ` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANG_ID` | [MIC_REF_ANG](MIC_REF_ANG.md) | `ANG_ID` |

