# CT_TYPE_COMMITTEE_RELTN

> This table contains the default selected committees for protocol participation types.

**Description:** Participation type and committee relationship table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AMD_VALIDATE_IND` | DOUBLE | NOT NULL |  | Default required value for amendments. |
| 3 | `COMMITTEE_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the committee table. This field identifies the commitee that is related to the protocol amendment. |
| 4 | `CT_TYPE_COMMITTEE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Ct_type_committee_reltn table. It is an internal system assigned number. |
| 5 | `EDIT_IND` | DOUBLE | NOT NULL |  | This field indicates whether this committee on this participation type can be edited |
| 6 | `PARTICIPATION_TYPE_CD` | DOUBLE | NOT NULL |  | This field indicates the type of participation available to protocols. |
| 7 | `REV_VALIDATE_IND` | DOUBLE | NOT NULL |  | Default required value for revisions. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMITTEE_ID` | [COMMITTEE](COMMITTEE.md) | `COMMITTEE_ID` |

