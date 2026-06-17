# RC_GSR_SUM_AGG_TMP

> This tables is used in the GSR summarization process to control the distributed summarization of data based on all possible values of an extract-specific dimension.

**Description:** Revenue Cycle Gold Standard Reporting Summary Aggregate Temporary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DATE` | DOUBLE | NOT NULL |  | The date for which activity data is to be summarized. |
| 2 | `AGGREGATE_INFO` | VARCHAR(250) | NOT NULL |  | This is a delimited string that defines the names of the source activity table, the column in that table containing the dimension id found in the attribute_value and the name of the dimension table for which this value represents the primary key. |
| 3 | `ATTRIBUTE_VALUE` | DOUBLE | NOT NULL |  | The value of a specific dimension id by which activity data is to be summarized. This value may be 0.0 to allow summarization to occur for activity data for which there is no related dimension row. See the aggregate_info column for information defining which dimension table is referenced, what it's primary key column name is, and what the name of the activity table being summarized is. |
| 4 | `LOAD_SCRIPT_NAME` | VARCHAR(32) | NOT NULL |  | The name of the load script that is responsible for summarizing the data associated with this row. |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `RCR_GSR_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related GSR Context Identifier |
| 7 | `TEMP_ID` | DOUBLE | NOT NULL |  | A sequential identifier for the rows that are inserted by the GSR summary load process for the logical_domain_id in which the process is being executed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCR_GSR_CONTEXT_ID` | [RCR_GSR_CONTEXT](RCR_GSR_CONTEXT.md) | `RCR_GSR_CONTEXT_ID` |

