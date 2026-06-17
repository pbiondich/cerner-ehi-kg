# OMF_COMP_FACT

> Comparison facts used by PowerVision.

**Description:** OMF COMP FACT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CF_INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator_cd for the fact from the saved view being referred to. This can come from a number of code sets depending on the team developing the subject area - e.g. 14265. |
| 2 | `CF_OMF_PV_ITEM_ID` | DOUBLE | NOT NULL |  | ID in omf_pv_items of the saved view being referred to. |
| 3 | `CF_SEQ1` | DOUBLE |  |  | Not currently used. Will be used if TAT comparison facts are allowed in PowerVision |
| 4 | `CF_SEQ2` | DOUBLE |  |  | Not currently used. Will be used if TAT comparison facts are allowed in PowerVision |
| 5 | `GRID_CD` | DOUBLE | NOT NULL |  | Subject area which this comparison fact is displayed in. The subject area of the saved view which displays this as a comparison fact not the saved view in cf_omf_pv_item_id. Code set 14265 is sometimes used but will vary by which Cerner team created the subject area. |
| 6 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Comparison fact indicator. Code set 14265 is sometimes used but will vary by which Cerner team created the subject area. |
| 7 | `NAME` | VARCHAR(50) |  |  | Display name of the comparison fact. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `USER_ID` | DOUBLE | NOT NULL |  | Users person_id who created the comparison fact. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

