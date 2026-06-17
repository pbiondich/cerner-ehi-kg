# DRC_FORM_RELTN_VER

> Provides History of the DRC_FORM_RELTN table.

**Description:** DRC FORM RELTN VER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BUILD_FLAG` | DOUBLE |  |  | A flag showing the how the relationship between MMDC's and Premise groups was built: |
| 3 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL |  | The id of the premise group/ dose ranges to be used in to DRC the order. |
| 4 | `DRC_FORM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique Identifier with ver_seq |
| 5 | `DRC_GROUP_ID` | DOUBLE | NOT NULL |  | The DRC grouping number that this set of dose range rules relates to |
| 6 | `FORMULATION_CODE` | DOUBLE |  |  | In the Multum world the MMDC id of the drug to be checked. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VER_SEQ` | DOUBLE | NOT NULL |  | History of the DRC_FORM_RELTN table |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

