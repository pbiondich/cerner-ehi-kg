# PCS_FRMT_VRSN_ELEMENT

> This table identifies elements that are embedded in a result layout format.

**Description:** PathNet Common Services Format Version Element  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `ELEMENT_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the element code embedded in the result layout format. |
| 4 | `ELEMENT_SEARCH_TEXT` | VARCHAR(100) | NOT NULL |  | Provides the ability to match the element in the result layout format. |
| 5 | `ELEMENT_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The unique sequential identifier of the element within the element list. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PCS_FRMT_VRSN_ELEMENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies elements that are embedded in a result layout format. |
| 8 | `PCS_RSLT_FRMT_VRSN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the version of the result layout format related to this element. |
| 9 | `PREV_PCS_FRMT_VRSN_ELEMENT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS Format Version Element information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCS_RSLT_FRMT_VRSN_ID` | [PCS_RSLT_FRMT_VRSN](PCS_RSLT_FRMT_VRSN.md) | `PCS_RSLT_FRMT_VRSN_ID` |

