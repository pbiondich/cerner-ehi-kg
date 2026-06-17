# DA_DOCUMENT_PRSNL_RELTN

> An optional association between a document and prsnl members or prsnl groups. This will be used to control access to documents in a user's inbox of Discern Analytics 2.0.

**Description:** Discern Analytics Document Personnel Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `DA_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The document this personnel member or personnel group is associated with. |
| 4 | `DA_DOCUMENT_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_DOCUMENT_PRSNL_RELTN table. |
| 5 | `DELIVERY_DT_TM` | DATETIME |  |  | The date and time the document was delivered to the document inbox. |
| 6 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The personnel group that is associated with the document. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel member that is associated with the document. |
| 8 | `READ_CHANGE_DT_TM` | DATETIME |  |  | The date and time the personnel member changed the read / unread status. |
| 9 | `READ_IND` | DOUBLE | NOT NULL |  | Flag to indicate whether the document has been read by the personnel member. |
| 10 | `REQUESTED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Represents the prsnl that requested the new document / prsnl relationship (in this case, it is the user that either manually marked the document to be saved to a certain prsnl / prsnl group or the user that scheduled the document for execution) |
| 11 | `SHORT_DESC` | VARCHAR(200) | NOT NULL |  | A description of, or reason for, the selected document being sent, as defined by the user responsible for the document being sent. For display in the DA2 Document Inbox. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_DOCUMENT_ID` | [DA_DOCUMENT](DA_DOCUMENT.md) | `DA_DOCUMENT_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUESTED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

