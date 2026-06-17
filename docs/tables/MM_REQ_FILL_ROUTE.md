# MM_REQ_FILL_ROUTE

> stores the association of requesting location and its fill location (for internal fill) as well as its purchasing and receiving profile (for external fill).

**Description:** Materials Management Requisition Fill Route  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Class Node ID value. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 5 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 6 | `FILL_LOC_CD` | DOUBLE | NOT NULL |  | The internal location from where the requisition is to be filled. |
| 7 | `FILL_LOC_SEQ` | DOUBLE |  |  | The sequence of the fill location, the smaller sequence will be chosen first if it qualifies. |
| 8 | `IN_TRANSIT_IND` | DOUBLE | NOT NULL |  | In-Transit functionality tracks that ordered goods/items have been received in the requesting location but still not delivered to the delivery location. This column indicates if this functionality in mmreqrouting.exe is supported for the specified location. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item |
| 10 | `ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of item that is being requisitioned. Can be item master, equipment master, medication definition or all 3 types. |
| 11 | `LOC_HIERARCHY_FLAG` | DOUBLE | NOT NULL |  | Indicates which workflow this location hierarchy was built for. |
| 12 | `MM_REQ_FILL_ROUTE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that uniquely identifies a single row on the MM_REQ_FILL_ROUTE table. |
| 13 | `POINT_OF_USE_IND` | DOUBLE | NOT NULL |  | Identifies rows that belong to the POU workflow. |
| 14 | `PUR_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The Purchase Profile associated to the requisition location. |
| 15 | `RCV_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Receiving Profile associated to the requisition location. |
| 16 | `REQ_LOC_CD` | DOUBLE | NOT NULL |  | Requisition Location Code Value |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PUR_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |
| `RCV_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |

