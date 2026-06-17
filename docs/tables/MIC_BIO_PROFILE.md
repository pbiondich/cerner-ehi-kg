# MIC_BIO_PROFILE

> This reference table contains a combination of an organism and group biochemical for which percent positive data is defined. The actual percent positive data is contained in the MIC_BIO_PROFILE_DETAIL table.

**Description:** Microbiology Biochemical Profile  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FREQUENCY_VALUE` | DOUBLE | NOT NULL |  | This field contains the 'typical profile' value for the group biochemical/organism combination. |
| 2 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the group biochemical. |
| 3 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the organism. |
| 4 | `PROFILE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code that uniquely identifies the 'percent positive' data for a group biochemical/organism combination. This value is used to join to the MIC_BIO_PROFILE_DETAIL table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

